# Learn about Input and Data Conversion

str_num_a = input('Digite o primeiro número: ')
str_num_b = input('Digite o segundo número: ')

num_a = float(str_num_a) # Converte string em decimal
num_b = float(str_num_b)

total = num_a + num_b
print(total)

# DataTyoes Functions

# str()
# float()
# int()
# bool()

# list()
# tuple()
# set()
# dict()

# Convert DataTypes: 

# Numbers
x = 10
str_x = str(x)          # Converte inteiro para string '10'
float_x = float(x)      # Converte inteiro para decimal: 10.0
bool_x = bool(x)        # Converte inteiro para boolean: True
bool_neg_x = bool(0)    # Converte 0 para boolean: False

# Strings
s = '123'               
int_s = int(s)          # Converte string para inteiro
float_s = float(s)      # Converte string para decimal
bool_s = bool(s)        # Converte string para boolean: True
bool_empty = bool(" ")  # Converte string vazia para boolean: False

# Booleans
bool_true = bool(1)         # True    
bool_false = bool(0)        # False
bool_list = bool([])        # Converte uma lista vazia em boolean: False
bool_dict = bool({})        # Converte um dict vazio em boolean: False
bool_str = bool("Hello")    # Converte non-empty string em boolean: True

# uma lista vazia é considerado falso, mas se tiver [[],[]] é considerado verdadeiro (msm coisa para dicionarios)
# se tiver qualquer dado é retornado verdadeiro

