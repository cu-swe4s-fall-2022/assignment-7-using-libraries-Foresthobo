# libraries
data_processor.py has functions to create a random matrix of size (N,M), a function to read the dimensions of a file, and a function to write a random matrix to a file

plotter.py is a script that takes the iris data set and creates 3 plots, a box plot, a scatter plot, and a multipanel plot of both all in 3 seperate .png files

added a new file path to try and fix an issue with my CI

## Example usage
get_random_matrix(10,10)
get_file_dimensions(file_name)
write_random_matrix(10, 10, file_name)