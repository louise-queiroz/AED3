import base64
import binascii

def base64_to_hex(base64_string):
    try:
        decoded_bytes = base64.b64decode(base64_string, validate=True)
        hex_string = decoded_bytes.hex()
        return hex_string
    except (binascii.Error, binascii.Incomplete):
        print("Erro: A entrada não é uma string base64 válida.")
        return None

# Exemplo de uso
base64_input = "ycW0hfWPJY4/sBBDiILGYGDJl+gaD7zZSXHaFG6trLiLuLWXi95UaSd45QqFITNRvS7FCa8E12rcppKUJtFmlCR6g8MkUIi2+NG7pz5v1Aa0vulDgGdr6pQNYS0MZg61+FXSI5dvKQH5vcsf/KWBcZ1n0a6DQJk8dX6T2fJygoZA8E5/L0W0jNR7XupjOl2wdkce8NzNDjwFvD3tsi+iOw=="  # Insira sua string base64 aqui
hex_output = base64_to_hex(base64_input)

if hex_output:
    print("Texto em base64:", base64_input)
    print("Texto em hexadecimal:", hex_output)
