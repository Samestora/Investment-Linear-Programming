import numpy as np
from scipy.optimize import linprog
from flask import Flask, render_template, request

app = Flask(__name__)

# Koefisien untuk fungsi objektif (negatif karena kita memaksimalkan keuntungan)
c = [-0.1, -0.05, -0.07]  # -P(x,y,z) = - 0.1x - 0.05y - 0.07z

# Matriks koefisien untuk batasan
A = [[1, 1, 1],    # Total investasi -> x + y + z <= 150000
     [1, 0, 0],  # Maksimum investasi di saham -> x + 0y + 0z <= 60000 -> x <= 60000
     [0, -1, 0], # Minimum di obligasi
     [0, 0, -1]]    # Minimum investasi di properti -> 0x + 0y + -z >= -45000

# Batas untuk variabel investasi (harus non-negatif)
bounds = [(0, None), (0, None), (0, None)]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ambil nilai dari form input
        b_values = [
            float(request.form['pool']),
            float(0.5 * float(request.form['pool'])),
            float(0.15 * -1 *float(request.form['pool'])),
            float(0.25 * -1 *float(request.form['pool']))
            ]
        
        # Hitung hasil linear programming dengan data input baru
        result = linprog(c, A_ub=A, b_ub=b_values, bounds=bounds, method="highs")
        
        if result.success:
            investment_in_shares, investment_in_bonds, investment_in_property = result.x
            profit = -result.fun
            return render_template('index.html',
                                   investment_in_shares=investment_in_shares,
                                   investment_in_bonds=investment_in_bonds,
                                   investment_in_property=investment_in_property,
                                   profit=profit)
        else:
            return "Solusi tidak ditemukan."

    return render_template('index.html', investment_in_shares=None, investment_in_bonds=None, investment_in_property=None, profit=None)

if __name__ == '__main__':
    app.run(debug=True)

