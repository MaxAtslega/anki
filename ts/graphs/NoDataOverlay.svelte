<!--
Copyright: Ankitects Pty Ltd and contributors
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
-->
<script lang="ts">
    import type { GraphBounds } from "./graph-helpers";
    import * as tr from "../lib/ftl";

    export let bounds: GraphBounds;

    const noData = tr.statisticsNoData();
</script>

<g class="no-data">
    <rect x="0" y="0" width={bounds.width} height={bounds.height} />
    <text x="{bounds.width / 2}," y={bounds.height / 2}>{noData}</text>
</g>

<style lang="scss">
    .no-data {
        rect {
            fill: var(--window-bg);
        }

        text {
            text-anchor: middle;
            fill: grey;
        }
    }
</style>
