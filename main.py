import numpy as np
from scipy.optimize import linprog
from flask import Flask, render_template, request

app = Flask(__name__)

# Koefisien untuk fungsi objektif (negatif karena kita memaksimalkan keuntungan)
c = [-0.1, -0.05, -0.07]

# Matriks koefisien untuk batasan
A = [[1, 1, 1],    # Total investasi
     [-1, 0, 0],   # Minimum investasi di saham
     [0, 0, 1]]    # Maksimum investasi di properti
b = [150000, -60000, 45000]

# Batasan untuk keuntungan tahunan minimal
A_eq = [[0.1, 0.05, 0.07]]
b_eq = [10000]

# Batas untuk variabel investasi (harus non-negatif)
bounds = [(0, None), (0, None), (0, None)]

result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")

# Hasil
if result.success:
    investment_in_shares, investment_in_bonds, investment_in_property = result.x
    print(f"Jumlah investasi di saham: ${investment_in_shares:.2f}")
    print(f"Jumlah investasi di obligasi: ${investment_in_bonds:.2f}")
    print(f"Jumlah investasi di properti: ${investment_in_property:.2f}")
else:
    print("Solusi tidak ditemukan.")

@app.route('/')
def index():
    return render_template('index.html',
                           investment_in_shares=investment_in_shares,
                           investment_in_bonds=investment_in_bonds,
                           investment_in_property=investment_in_property
                           )
if __name__ == '__main__':
    app.run(debug=True)
