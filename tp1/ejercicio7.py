# Programar una función Python que procese el contenido de un archivo .csv con las columnas
# [id, first_name, last_name, email, gender, avatar, job_title, language, ssn] y genere un nuevo archivo .csv

# a) -> se cambiará el orden las columnas first_name y last_name y se elimina gender
#       quedando: [id, last_name, first_name, email, avatar, job_title, language, ssn]

# b) -> y se modificara el dominio en las direcciones de correo, sustituyendo el dominio actual
#       (parte derecha luego del símbolo @) por @ing.unlpam.edu.ar

import csv
import re


def convert(input_file_path: str, output_file_path: str) -> None:
    if len(input_file_path) == 0 and len(output_file_path) == 0:
        return None

    with open(input_file_path, "r", newline="", encoding="utf-8") as input_file, open(
        output_file_path, "w", newline="", encoding="utf-8"
    ) as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        for line_with_info in reader:
            if "first_name" and "last_name" and "gender" in line_with_info:
                # position_first_name = line_with_info.index("first_name")
                # position_last_name = line_with_info.index("last_name")
                # position_gender = line_with_info.index("gender")
                # position_email = line_with_info.index("email")
                pass

            #
            position_first_name = 1
            position_last_name = 2
            position_gender = 4
            position_email = 3

            # Acá realizo el ejercicio a)
            line_with_info[position_first_name], line_with_info[position_last_name] = (
                line_with_info[position_last_name],
                line_with_info[position_first_name],
            )
            del line_with_info[position_gender]

            # Acá realizo el ejercicio b)
            target = r"@.*"
            replace = "@ing.unlpam.edu.ar"
            line_with_info[position_email] = re.sub(
                target, replace, line_with_info[position_email]
            )

            writer.writerow(line_with_info)

        input_file.close()
        output_file.close()
