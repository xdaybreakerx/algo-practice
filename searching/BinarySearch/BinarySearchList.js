export default function bs_list(haystack, needle) {
    let lo = 0;
    let hi = haystack.length;

    do {
        const mid = Math.floor(lo + (hi - lo) / 2);
        const val = haystack[mid];

        if (val === needle) {
            return true;
        } else if (val > needle) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    } while (lo < hi);
    return false;
}
