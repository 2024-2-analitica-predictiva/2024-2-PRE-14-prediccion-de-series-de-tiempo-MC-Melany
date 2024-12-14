{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "import numpy as np  #  type: ignore\n",
    "import matplotlib.pyplot as plt  #  type: ignore\n",
    "import pandas as pd  #  type: ignore\n",
    "\n",
    "from sklearn.metrics import mean_squared_error, mean_absolute_error\n",
    "from statsmodels.tsa.stattools import acf, pacf  #  type: ignore\n",
    "from statsmodels.graphics.tsaplots import plot_acf, plot_pacf  #  type: ignore\n",
    "\n",
    "\n",
    "\n",
    "  \n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_data():\n",
    "    df = pd.read_csv(\"../files/input/sutter.csv\")\n",
    "    df = df.set_index(\"date\")\n",
    "    return df\n",
    "  "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
