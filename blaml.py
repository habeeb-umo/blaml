import os, shutil
input_file = open('test.yaml', 'r')

output = None
output_filenames = []
yaml_filenames = []
count = 0

if os.path.exists('./output'):
    shutil.rmtree('./output')
os.makedirs('./output')

for line in input_file:
    if line == '---\n':
        if output and count > 0:
            output.close()
        output_name = './output/output' + str(count) + '.yaml'
        output_filenames.append(output_name)
        output = open(output_name, 'w')

    # Find/store chart name from metadata
    if line.startswith('  name:'):
        yaml_name = line[8:len(line)-1]
        yaml_filenames.append('./output/' + yaml_name + '.yaml')

    output.write(line)
    count += 1

for file in output_filenames:
    # Remove file if less than 5B (means that its a file with only --- or empty)
    if os.path.getsize(file) < 5:
        os.remove(file)
        output_filenames.remove(file)
        continue

    # Rename output files to chart_name.yaml
    os.rename(file, yaml_filenames.pop(0))
