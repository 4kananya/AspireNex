## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/).

### Installation

1. **Clone the Repository**

   Clone this repository to your local machine

2. **Navigate to the Repository Directory**

   ```bash
   cd recommendation-system
   ```

3. **Install the Required Libraries**

   Install the required Python libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

### Download Datasets

Download the required datasets from Kaggle:

1. **Book Recommendation Dataset**

   Download the Book Recommendation Dataset from [this link](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset).

2. **TMDB Movie Metadata**

   Download the TMDB Movie Metadata dataset from [this link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv).

### Update Paths in the Notebook

Open the `Recommendation_System.ipynb` notebook and update the paths to the downloaded datasets accordingly. 

### Run the Notebook

Run the Jupyter notebook to build and evaluate the recommendation system. 

You can start Jupyter Notebook by running:

```bash
jupyter notebook
```

Then, open `Recommendation_System.ipynb` and run all the cells.

### Run the Streamlit App

After updating the dataset paths and running the notebook, you can run the Streamlit app by executing the following command:

```bash
streamlit run recommendation_system.py
```

This will start the Streamlit server, and you can interact with the recommendation system through your web browser.

## Acknowledgments

- Kaggle for providing the datasets.
- The open-source community for their invaluable libraries and tools.
