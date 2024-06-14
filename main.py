import read_data
import constants

def main():
    data = read_data.read_from_csv_to_data(constants.DATA_FILE)
    read_data.generate_graph(16,15,data)

if __name__ == "__main__":
    main()
