func reverseString(s []byte) {
    i := 0
    j := len(s) -1
    for j - i > 0 {
        if s[i] != s[j] {
            s[i], s[j] = s[j], s[i]
        }
        i++
        j--
    }
}
