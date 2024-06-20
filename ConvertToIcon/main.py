# Converte uma imagem em qualquer formato, para .ico nas dimensões informadas. Geralmente icone
# de programa é 64x64
from PIL import Image


def converter_imagem(input_path, output_path, tamanho=(64, 64)):
    # Abrir a imagem
    imagem = Image.open(input_path)

    # Redimensionar a imagem
    imagem_redimensionada = imagem.resize(tamanho)

    # Converter para o formato desejado (PNG, JPEG, etc.)
    imagem_redimensionada.save(output_path)

    # Criar o ícone (.ico)
    imagem_redimensionada.save(output_path.replace('.png', '.ico'))


# Exemplo de uso
if __name__ == "__main__":
    # Caminho da imagem de entrada
    input_path = "caminho/para/sua/imagem.png"

    # Caminho de saída para a imagem redimensionada
    output_path = "caminho/de/saida/imagem_redimensionada.png"

    # Chamar a função para converter e redimensionar a imagem
    converter_imagem(input_path, output_path)

