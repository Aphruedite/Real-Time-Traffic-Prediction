# Importing Necessary Libraries
import pickle
import scipy.io

# Function to load and prepare the data
def load_and_prepare_data(file_path):
    # Load the .mat file using the provided file path
    mat = scipy.io.loadmat(file_path)
    
    # Extract training and testing data
    tra_X_tr = mat['tra_X_tr']
    tra_Y_tr = mat['tra_Y_tr']
    tra_X_te = mat['tra_X_te']
    tra_Y_te = mat['tra_Y_te']
    tra_adj_mat = mat['tra_adj_mat']
    
    # Save the data using pickle for later use
    with open('tra_X_tr.pkl', 'wb') as f:
        pickle.dump(tra_X_tr, f)
    
    with open('tra_Y_tr.pkl', 'wb') as f:
        pickle.dump(tra_Y_tr, f)
    
    print("Data preparation complete. Data saved as pickle files.")

# Usage
load_and_prepare_data("/Users/rujutaparulekar/Desktop/OpAI/traffic_dataset.mat")
