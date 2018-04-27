load('../outputs/generator_matrix_16.sage')

code = codes.LinearCode(generator_matrix)

print('length = {}'.format(code.length()))
print('dimension = {}'.format(code.dimension()))
print('spectrum = {}'.format(code.spectrum()))
