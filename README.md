# Tarefa RSA e AES
Como criptoanalista no Biuro Szyfrów, você interceptou uma mensagem cifrada, criptografada com AES 256 bits, cuja chave (presente no arquivo key_for_message.en) foi criptografada utilizando uma chave pública RSA. Você adquiriu a chave pública, mas ela está encriptada com AES256 também! Você enviou um dos seus melhores agentes para obter essa chave,  mas dos doze caracteres da senha, ele descobriu apenas os dois primeiros: "do", antes de ser capturado.  Em sua última transmissão, ele conseguiu lhe enviar a hash da senha (presente no arquivo key_for_rsa_public.hash). Muito provavelmente foi utilizado um algoritmo de hash famoso para ocultar a senha...

Você tem acesso aos seguintes items: mensagem cifrada, chave usada para encriptar a mensagem (mas encriptada), chave pública RSA (mas encriptada), e hash da chave utilizada para encriptar a chave pública.

Sabe ainda que provavelmente foi utilizado o programa openssl para realizar as encriptações.

Sua tarefa é obter a mensagem cifrada.
