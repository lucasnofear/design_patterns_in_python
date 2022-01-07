from document import Document

# creating a document containing a list of two lists
original_document = Document("Original", [[1, 2, 3, 4], [5, 6, 7, 8]])
print(original_document)
print()

document_copy_1 = original_document.clone(1)
document_copy_1.name = "Copy 1"
document_copy_1.list[1][2] = 200
print(document_copy_1)
print(original_document)
print()

document_copy_2 = original_document.clone(2)
document_copy_2.name = "Copy 2"
document_copy_2.list[1] = [9, 10, 11, 12]
print(document_copy_2)
print(original_document)
print()

document_copy_3 = original_document.clone(2)
document_copy_3.name = "Copy 3"
document_copy_3.list[1][0] = "1234"
print(document_copy_3)
print(original_document)
print()

document_copy_4 = original_document.clone(3)
document_copy_4.name = "Copy 4"
document_copy_4.list[1][0] = "5678"
print(document_copy_4)
print(original_document)