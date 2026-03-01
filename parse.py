from unstructured.partition.pdf import partition_pdf
from unstructured.documents.elements import Element, Image, Text, Table


def parse(path: str) -> list[Element]:
    elements = partition_pdf(
        filename=path,
        strategy="hi_res",
        infer_table_structure=True,
        extract_image_block_types=["Image", "Figure", "Table"],
        extract_image_block_to_payload=True,
        chunking_strategy=None,
    )
    return elements


if __name__ == "__main__":
    path = "/home/arjav.singh/Projects/hr-rag/documents/2312.10997v5.pdf"
    elements = parse(path)

    # Print the number of elements parsed
    print(f"Number of elements parsed: {len(elements)}")

    # Print the first few elements for inspection
    for i, element in enumerate(elements[:5]):
        print(f"Element {i}: {type(element).__name__} - {element.text[:100]}")
