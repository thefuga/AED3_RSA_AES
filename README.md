# Tarefa: RSA e AES

Como criptoanalista no Biuro Szyfrów, você interceptou uma mensagem cifrada, criptografada com AES 256 bits, cuja chave foi criptografada utilizando uma chave pública RSA. Você tem acesso tanto a mensagem cifrada como a chave cifrada. Sabe ainda que provavelmente foi utilizado o programa openssl para realizar ambas encriptações.

Sua tarefa é obter a mensagem cifrada.

Ao concluir a tarefa, submeta os procedimentos adotados que permitam replicar o processo, bem como a senha e a mensagem originais, em um único arquivo PDF.

A nota deste trabalho comporá 20% da nota final da disciplina. Será avaliado da seguinte forma:

- Nota máxima para os trabalhos corretos entregues até o dia 27/11;
- 85% da nota máxima para trabalhos corretos entregues até o dia 01/12;
- Cada trabalho correto entregue até 01/12 receberá até 2,0 pontos adicionais. Este bônus de 2 pontos será dividido pelo número de trabalhos corretos entregues pela turma.


# Solução:

**Mensagem descriptografada:**
    We intend to begin on the first of February unrestricted submarine warfare. We shall endeavor in spite of this to keep the United States of America neutral. In the event of this not succeeding, we make Mexico a proposal of alliance on the following basis: make war together, make peace together, generous financial support and an understanding on our part that Mexico is to reconquer the lost territory in Texas, New Mexico, and Arizona. The settlement in detail is left to you. You will inform the President of the above most secretly as soon as the outbreak of war with the United States of America is certain and add the suggestion that he should, on his own initiative, invite Japan to immediate adherence and at the same time mediate between Japan and ourselves. Please call the President's attention to the fact that the ruthless employment of our submarines now offers the prospect of compelling England in a few months to make peace.

    Signed, ZIMMERMANN.

**Chave AES:**
    6AYwFJffIFVVpYkCUFf4Jw==

**Chave RSA privada:**
    -----BEGIN RSA PRIVATE KEY-----
    MIHBAgEAAiYOWxON4VVOCjgECz38THnFRTqJY2gENjwnu266/sg0yYw6BiggVQID
    AQABAiYKAICuQInrtojyoFaOm0XYIPS4gdMeNj3C5uWo2IfKGNERZ8+4AQITPX2s
    M0jDhgm4ndB+ijBfokJuAQITO8QkAkcydrUiO+qEJlMfWe2aVQITFVxIq3AFa9SI
    q1m3+20ea5FEAQITL1bOxtcqC4ixkw/QmKKiZJKk+QITA+HQAN0Pyy+LQVUdHZPk
    Xcku+Q==
    -----END RSA PRIVATE KEY-----

**Passos para a solução do problema:**
Para a solução do problema, foi criado um programa em Python (pycrypto.py), que utiliza a biblioteca PyCrypto, para encontrar um mod "n" e um expoente "e" a partir da chave pública pub.key.
A partir daí, foi utilizado o programa msieve para fatorar "n". O resultado obtido após rodar o programa foi:
    p46 factor: 1332830227949273521465367319234277279439624789
    p46 factor: 1371293089587387292180481293784036793076837889
    elapsed time 00:32:37

Após isso, no programa criado, foi utilizada a função invert() da biblioteca gmpy2 para obter o expoente a partir destes dois números primos. Com isso, foi gerada a chave privada, e posteriormente, exportada para o arquivo private.pem.
Com a chave RSA privada, foi possível descriptografar a chave AES, utilizando o programa openssl. Para isso, foi utilizado o comando:
    openssl rsautl -decrypt -in key.cipher -out aes_decrypted_key.txt -inkey private.pem
Onde aes_decrypted_key.txt é o arquivo contendo a chave AES/senha.
Feito isso, bastava descriptografar a mensagem. Isso foi feito utilizando o openssl com o seguinte comando:
    openssl aes-256-cbc -d -a -in ciphertext.enc -out decrypted_text.txt
Após a execução do comando, a chave AES/senha (contida em aes_decrypted_key) foi solicitada.
Com isso, o arquivo decrypted_text.txt foi criado, contendo a mensagem descriptografada.

**Fontes que auxiliaram na solução do problema:**
    https://warrenguy.me/blog/regenerating-rsa-private-key-python
    https://www.dlitz.net/software/pycrypto/
    https://sourceforge.net/projects/msieve/
    http://tombuntu.com/index.php/2007/12/12/simple-file-encryption-with-openssl/
