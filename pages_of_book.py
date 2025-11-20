def find_page_count(K):
    digits = 0
    length = 1
    count = 9
    total_pages = 0
    while K >= count * length:
        K -= count * length
        total_pages += count
        length += 1
        count *= 10
    total_pages += K //length
    return total_pages
K = int(input("Enter the common count of pages:"))
N = find_page_count(K)
print("The count of pages in the book is:", N)