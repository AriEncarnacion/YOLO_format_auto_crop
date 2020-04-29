def get_labels(labels_path, labels_dir):
    all_labels = []
    for file in labels_dir:
        labels = []
        if file.endswith(".txt"):
            f_path = labels_path + file

            print("opening file at path:", f_path)
            with open(f_path) as f:
                data = f.readlines()
                for line in data:
                    labels.append(line.strip().split(" "))

            for row in labels:
                print(row)

            all_labels.append(labels)
            print()
    print("LABEL PARSING SUCCESSFULLY COMPLETED.")
    print()

    return all_labels
