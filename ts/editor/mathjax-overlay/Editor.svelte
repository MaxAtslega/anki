<!--
Copyright: Ankitects Pty Ltd and contributors
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
-->
<script lang="ts">
    import { onMount, createEventDispatcher } from "svelte";
    import { ChangeTimer } from "../change-timer";
    import { CodeMirror, latex, baseOptions } from "../code-mirror";

    export let initialValue: string;

    const codeMirrorOptions = {
        mode: latex,
        ...baseOptions,
    };

    let codeMirror: CodeMirror.EditorFromTextArea;
    const changeTimer = new ChangeTimer();
    const dispatch = createEventDispatcher();

    function onInput() {
        dispatch("update", { mathjax: codeMirror.getValue() });

        /* changeTimer.schedule( */
        /*     () => dispatch("update", { mathjax: codeMirror.getValue() }), */
        /*     400 */
        /* ); */
    }

    function onBlur() {
        changeTimer.fireImmediately();
        dispatch("codemirrorblur");
    }

    function openCodemirror(textarea: HTMLTextAreaElement): void {
        codeMirror = CodeMirror.fromTextArea(textarea, codeMirrorOptions);
        codeMirror.on("change", onInput);
        codeMirror.on("blur", onBlur);
    }

    let textarea: HTMLTextAreaElement;

    onMount(() => {
        codeMirror.focus();
        codeMirror.setCursor(codeMirror.lineCount(), 0);

        const codeMirrorElement = textarea.nextElementSibling!;
        codeMirrorElement.classList.add("mathjax-editor");
    });
</script>

<div
    on:click|stopPropagation
    on:focus|stopPropagation
    on:focusin|stopPropagation
    on:keydown|stopPropagation
    on:keyup|stopPropagation
    on:mousedown|preventDefault|stopPropagation
    on:mouseup|stopPropagation
    on:paste|stopPropagation
>
    <!-- TODO no focusin for now, as EditingArea will defer to Editable/Codable -->
    <textarea
        bind:this={textarea}
        value={initialValue}
        on:input={onInput}
        use:openCodemirror
    />
</div>

<style lang="scss">
    div :global(.mathjax-editor) {
        border-radius: 0;
        border-width: 0 1px;
        border-color: var(--medium-border);

        height: auto;
        border-radius: 0 0 5px 5px;
        padding: 6px 0;
    }
</style>
