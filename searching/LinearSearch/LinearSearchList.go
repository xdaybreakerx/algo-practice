package main

func linearSearch(
	haystack []int,
	needle int) bool {
	for i := range haystack {
		if haystack[i] == needle {
			return true
		}
	}
	return false
}
