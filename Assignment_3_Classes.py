#Firstly we import the pyplot module
import matplotlib.pyplot as plt

#Writing the class statement
class Coordinate_translator:

#Dictating the information to create a coordinate_translator object
    def __init__(self, coordinates_txt_file):

#Initializing the class with a coordinate txt file
        self.coordinates_txt_file = coordinates_txt_file
        self.x_data = []
        self.y_data = []
        self.translated_x_data = []
        self.translated_y_data = []

        self.load_coordinates()

#Defining a function that loads coordinates from the txt file
    def load_coordinates(self):
        with open(self.coordinates_txt_file, 'r') as file:
            next(file)
            for line in file:
                values = line.strip().split(',')
                if len(values) == 2:
                    try:
                        x_val = float(values[0])
                        y_val = float(values[1])
                        self.x_data.append(x_val)
                        self.y_data.append(y_val)
                    except ValueError:
                        print(f"could not convert values to float: {values}")
                else:
                    print(f"unexpected format of values: {values}")

#Defining a function that plots both the original and the translated coordinates
    def plot(self):

#Setting up properties of the scatterplot
        plt.scatter(self.x_data, self.y_data, color='blue', label='original data')
        plt.scatter(self.translated_x_data, self.translated_y_data, color='purple', label='translated data')
        plt.xlabel('x coordinates')
        plt.ylabel('y coordinates')
        plt.title('Scatterplot of original and translated coordinates')
        plt.grid(True)
        plt.legend()
        plt.show()

#To translate the points to specified destinations, dx and dy
    def translated_plot(self, dx, dy):
        self.translated_x_data = [x_data + dx for x_data in self.x_data]
        self.translated_y_data = [y_data + dy for y_data in self.y_data]

#To call the main function
if __name__ == "__main__":
    scatter_plotter = Coordinate_translator('C:/Users/TEVES/Downloads/x_y_coordinates.txt')
    scatter_plotter.translated_plot(3, 2)
    scatter_plotter.plot()