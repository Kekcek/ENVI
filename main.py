import os

def creating_root_folders(path_to_dir, name_folder):
    os.chdir(path_to_dir)
    os.makedirs(name_folder, exist_ok=True)


def creating_inside_folders(path_to_dir, name_folder, roi):
    os.chdir(path_to_dir)
    for i in range(1, roi + 1, 10):
        index_od_star = name_folder.find("*")
        name = name_folder[:index_od_star] + f"{i}-{i+9}" + name_folder[index_od_star + 1:]
        os.makedirs(name, exist_ok=True)

path_to_dir = input("Введите путь до папки: ")
number_object = input("Введите число, обозначающий номер объекта: ")
count_roi = int(input("Введите количество ROI: "))
name_main_folder = "N_tar-" + number_object + "_lin_AREA"

name_0_folder = "0_N_tar-" + number_object + "_lin_AREA"
name_1_folder = "1_N_tar-" + number_object + "_ROI"
name_2_folder = "2_N_tar-" + number_object + "_sl"
name_3_folder = "3_work_tar-" + number_object
name_4_folder = "4_N_tar-" + number_object + "_ROI_nz"

creating_root_folders(path_to_dir, name_main_folder)
path_to_dir = path_to_dir + r"\\" + name_main_folder

creating_root_folders(path_to_dir, name_0_folder)
creating_root_folders(path_to_dir, name_1_folder)
creating_root_folders(path_to_dir, name_2_folder)
creating_root_folders(path_to_dir, name_3_folder)
creating_root_folders(path_to_dir, name_4_folder)

inside_1_folder = "*_t-" + number_object
inside_2_folder = "sl_*_t-" + number_object
inside_4_folder = "*_t-" + number_object + "_nz_"

creating_inside_folders(path_to_dir + r"\\" + name_1_folder, inside_1_folder, count_roi)
creating_inside_folders(path_to_dir + r"\\" + name_2_folder, inside_2_folder, count_roi)
creating_inside_folders(path_to_dir + r"\\" + name_4_folder, inside_4_folder, count_roi)