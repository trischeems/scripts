using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AppTinhTienDien
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Phương thức tính tiền điện
        private double CalculateElectricityBill(double kWh)
        {
            double bill = 0;

            if (kWh <= 50)
            {
                bill = kWh * 1678;
            }
            else if (kWh <= 100)
            {
                bill = (50 * 1678) + ((kWh - 50) * 1734);
            }
            else if (kWh <= 200)
            {
                bill = (50 * 1678) + (50 * 1734) + ((kWh - 100) * 2014);
            }
            else if (kWh <= 300)
            {
                bill = (50 * 1678) + (50 * 1734) + (100 * 2014) + ((kWh - 200) * 2536);
            }
            else if (kWh <= 400)
            {
                bill = (50 * 1678) + (50 * 1734) + (100 * 2014) + (100 * 2536) + ((kWh - 300) * 2834);
            }
            else
            {
                bill = (50 * 1678) + (50 * 1734) + (100 * 2014) + (100 * 2536) + (100 * 2834) + ((kWh - 400) * 2927);
            }

            return bill;
        }

        private void buttonCalculate_Click(object sender, EventArgs e)
        {
            try
            {
                // Lấy số điện tiêu thụ từ textBox
                double kWh = Convert.ToDouble(textBoxKwh.Text);

                // Tính tiền điện và hiển thị kết quả
                double bill = CalculateElectricityBill(kWh);
                labelResult.Text = $"Số tiền điện phải trả là: {bill} VND";
            }
            catch (FormatException)
            {
                MessageBox.Show("Vui lòng nhập một số hợp lệ!", "Lỗi", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
