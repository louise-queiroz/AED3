from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Valores d, N e e
d = 9250237803670600095397030792993956121924183625312756243143629620629645992140334876796105403899232507411334974758573
N = 23639416453077017681888680330686094847437910791660054821881595270727886287143678572564492214551329027237275625734109
e = 65537

# Calculando p e q a partir de N
p = 4988586550946572698837659323141005331783499412890195822279  # Substitua pelo cálculo correto
q = 4738700273445489960492041313631971343000359635005034483771  # Substitua pelo cálculo correto

# Calculando as partes dmp1, dmq1 e iqmp
dmp1 = d % (p - 1)
dmq1 = d % (q - 1)
iqmp = pow(q, -1, p)  # Inverso multiplicativo modular de q em relação a p

# Criando a chave privada RSA
private_key = rsa.RSAPrivateNumbers(
    p=p, q=q, d=d, dmp1=dmp1, dmq1=dmq1, iqmp=iqmp, public_numbers=rsa.RSAPublicNumbers(e=e, n=N)
).private_key()

# Serializar a chave privada no formato PEM
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()  # Sem senha
)

# Salvar a chave privada no arquivo
with open("private_key.pem", "wb") as private_key_file:
    private_key_file.write(private_pem)

print("Chave privada gerada e salva em private_key.pem")

