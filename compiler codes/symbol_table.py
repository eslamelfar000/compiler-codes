# Define a dictionary to store the symbol table entries
symbol_table = {}

# Define data type bytes
data_types = {"int": 4, "char": 1, "bool": 2, "float": 4}

# Define a function to add a new entry to the symbol table
def add_entry(
    name, type, object_address, dimension_num, line_declaration, line_references
):
    symbol_table[name] = {
        "Type": type,
        "Object Address": object_address,
        "Dimension Num": dimension_num,
        "Line Declaration": line_declaration,
        "Line References": line_references,
    }

# Define a function to parse the input code and generate the symbol table
def parse_code(input_code):
    lines = input_code.split("\n")
    current_line = 1
    current_address = 0
    for line in lines:
        words = line.split()
        for i, word in enumerate(words):
            if word == "int" or word == "float" or word == "bool" or word == "char":
                # Found a variable declaration
                name = words[i + 1]
                type = word
                object_address = current_address
                dimension_num = 0
                line_declaration = current_line
                line_references = [current_line]
                add_entry(
                    name,
                    type,
                    object_address,
                    dimension_num,
                    line_declaration,
                    line_references,
                )
                typeValue = data_types[word]
                current_address += typeValue

                if (
                    len(words) > i + 2
                    and words[i + 2].startswith("[")
                    and words[i + 2].endswith("]")
                ):
                    # Found an array declaration
                    typeValue = data_types[word]
                    dimension_str = words[i + 2][1:-1]
                    dimension_num = len(dimension_str.split(","))
                    current_address += typeValue * dimension_num
            elif word in symbol_table:
                # Found a variable reference
                symbol_table[word]["Line References"].append(current_line)
        current_line += 1


# Test the code with the input example and print out the resulting symbol table
input_code = """
int arr[3,8,5];
float y;
bool z;
arr[0] = 1;
arr[1] = 2;
arr[2] = 3;
char m;
float x = arr[0] + arr[1];
if (x > y) {
    z = true;
} else {
    z = false;
}
int result = x * arr[2];
for (int i = 0; i < result; i++) {
    print(i);
}
"""
parse_code(input_code)

# Print out the resulting symbol table in table format
print(
    "| {:<16} | {:<16} | {:<16} | {:<16} | {:<16} | {:<16} |".format(
        "Name",
        "Type",
        "Object Address",
        "Dimension Num",
        "Line Declaration",
        "Line References",
    )
)
print(
    "|------------------|------------------|------------------|------------------|------------------|------------------|"
)
for name, entry in symbol_table.items():
    type = entry["Type"]
    object_address = entry["Object Address"]
    dimension_num = entry["Dimension Num"]
    line_declaration = entry["Line Declaration"]
    line_references = ", ".join(map(str, entry["Line References"]))
    print(
        "| {:<16} | {:<16} | {:<16} | {:<16} | {:<16} | {:<16} |".format(
            name, type, object_address, dimension_num, line_declaration, line_references
        )
    )
