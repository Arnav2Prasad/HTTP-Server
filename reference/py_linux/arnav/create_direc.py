import os

# Define the path of the directory you want to create
directory_path = "/path/to/your/directory"

# Use os.makedirs() to create the directory
try:
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory '{directory_path}' created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")


'''
The `exist_ok=True` parameter is used in the `os.makedirs()` function in Python to control the 
behavior when the target directory already exists. 

#`os.makedirs()` Function

The `os.makedirs()` function in Python is used to create a directory recursively. 
This means it can create intermediate-level directories needed to contain the leaf directory.

#`exist_ok` Parameter

- Purpose: The `exist_ok` parameter allows the function to avoid raising an error if the target directory already exists.
- Type: Boolean (`True` or `False`)
  - `exist_ok=True`: If the directory already exists, the function will not raise an error.
  - `exist_ok=False`: If the directory already exists, the function will raise a `FileExistsError`.


#Example Usage

Here is a simple example to illustrate the usage of `exist_ok`:


            import os
            
            # Define the path of the directory you want to create
            directory_path = "/path/to/your/directory"
            
            # Create the directory, avoiding error if it already exists
            try:
                os.makedirs(directory_path, exist_ok=True)
                print(f"Directory '{directory_path}' created successfully or already exists.")
            except Exception as e:
                print(f"An error occurred: {e}")


In this example:
- `os.makedirs(directory_path, exist_ok=True)`: This will create the directory at the specified path. If the directory already exists, 
        it will not raise an error.
- Without `exist_ok=True`:

              os.makedirs(directory_path)

  If the directory already exists, this would raise a `FileExistsError`.


#Practical Use

The `exist_ok=True` parameter is particularly useful in scenarios where:
- You want to ensure the directory structure exists without worrying about whether it already exists.
- You want to avoid cluttering your code with additional checks to see if the directory exists before attempting to create it.

In summary, `exist_ok=True` simplifies directory creation by handling the case where the directory might already exist, 
allowing your code to focus on other tasks without additional error handling for this specific case.

'''
