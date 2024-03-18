import os
import aspose.words as aw

# Path to the input directory containing the TXT files
input_dir = r'I:\\IVALIX\\TXT\\mei\\data\\in\\RAW'

# Path to the output directory to save the concatenated TXT file
output_dir = r'I:\\IVALIX\\TXT\\mei\\data\\in\\OK'

def join_txt():

    fileNames = [ "Input1.docx", "Input2.docx" ]

    output = aw.Document()
    # Remova todo o conteúdo do documento de destino antes de anexar.
    output.remove_all_children()

    for fileName in fileNames:
        input = aw.Document(fileName)
        # Anexe o documento de origem ao final do documento de destino.
        output.append_document(input, aw.ImportFormatMode.KEEP_SOURCE_FORMATTING)

    output.save("Output.pdf");
