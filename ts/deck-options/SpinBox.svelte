<!--
Copyright: Ankitects Pty Ltd and contributors
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
-->
<script lang="ts">
    import { getContext } from "svelte";
    import { nightModeKey } from "../components/context-keys";

    export let value: number;
    export let min = 1;
    export let max = 9999;

    const nightMode = getContext<boolean>(nightModeKey);

    function checkMinMax() {
        if (value > max) {
            value = max;
        } else if (value < min) {
            value = min;
        }
    }
</script>

<input
    type="number"
    pattern="[0-9]*"
    inputmode="numeric"
    {min}
    {max}
    bind:value
    class="spin-box form-control"
    class:nightMode
    on:blur={checkMinMax}
/>

<style lang="scss">
    @use "sass/night-mode" as nightmode;

    .spin-box {
        /* overwrite Bootstrap */
        padding: 0.2rem 0.75rem;
    }

    .nightMode {
        @include nightmode.input;
    }
</style>
