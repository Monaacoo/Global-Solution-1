import os
import sys
import base64

TARGET_SIGNATURE = "@author: r1g312"

OUTPUT = "decodificados"
AUTHOR_FILE = "author.txt"

def encode_base64(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def decode_base64(text):

    try:
        return base64.b64decode(text.encode('utf-8')).decode('utf-8')
    except Exception as e:

        print(f"Erro pra decodificar: {e}")
        return None

def process(input_dir):

    try:
        #Verifica
        if not os.path.exists(input_dir):
            print(f"A pasta '{input_dir}' não existe.")
            return
        
    except Exception as e:

        print(f"Erro: {e}")
        sys.exit(1)

    try:
        #cria e verifica se tem
        os.makedirs(OUTPUT, exist_ok=True)

    except Exception as e:

        print(f"Erro na saida '{OUTPUT}': {e}")
        sys.exit(1)

    author_found = False

    #coloquei 3 valores para não fazer a verificação de subfolders
    for folder,subfolder, files in os.walk(input_dir):
        try:
            #copia pasta
            relative = os.path.relpath(folder, input_dir)
            output_folder = os.path.join(OUTPUT, relative)
            os.makedirs(output_folder, exist_ok=True)

        except Exception as e:
            print(f"Erro pra criar pasta '{output_folder}': {e}")
            continue

        for file in files:
            #so .log
            if not file.endswith('.log'):
                continue

            join_file = os.path.join(folder, file)
            output_file = os.path.join(output_folder, file)

            try:
                #le
                with open(join_file, 'r') as k:
                    encoded_content = k.read()

            except Exception as e:
                print(f"Erro na leiutra do arquivo '{join_file}': {e}")
                continue

            #decode
            decoded_content = decode_base64(encoded_content)

            if decoded_content is None:
                continue

            try:
                #escreve e salva
                with open(output_file, 'w') as f:
                    f.write(decoded_content)

            except Exception as e:
                print(f"Erro pra escrever '{output_file}': {e}")
                continue

            found_file_path = ""
            #se achar, salva
            try:
                if TARGET_SIGNATURE in decoded_content and not author_found:
                    with open(AUTHOR_FILE, 'w') as f:
                        f.write(decoded_content)
                        f.write(f"\nNesse arquivo: {join_file}")
                    found_file_path = join_file
                    author_found = True
            except Exception as e:
                print(f"Erro: {e}")

    if not author_found:
        print("Encontramos nada.")

if __name__ == '__main__':
    try:
        input_directory = sys.argv[1]
        process(input_directory)
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)
