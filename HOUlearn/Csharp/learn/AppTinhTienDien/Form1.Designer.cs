namespace AppTinhTienDien
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.TextBox textBoxKwh;
        private System.Windows.Forms.Label labelResult;
        private System.Windows.Forms.Button buttonCalculate;

        // Khởi tạo và thêm các điều khiển vào form
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.textBoxKwh = new System.Windows.Forms.TextBox();
            this.labelResult = new System.Windows.Forms.Label();
            this.buttonCalculate = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // textBoxKwh
            // 
            this.textBoxKwh.Location = new System.Drawing.Point(20, 20);
            this.textBoxKwh.Name = "textBoxKwh";
            this.textBoxKwh.Size = new System.Drawing.Size(260, 20);
            this.textBoxKwh.TabIndex = 0;
            // 
            // labelResult
            // 
            this.labelResult.Location = new System.Drawing.Point(20, 100);
            this.labelResult.Name = "labelResult";
            this.labelResult.Size = new System.Drawing.Size(260, 20);
            this.labelResult.TabIndex = 1;
            // 
            // buttonCalculate
            // 
            this.buttonCalculate.Location = new System.Drawing.Point(20, 60);
            this.buttonCalculate.Name = "buttonCalculate";
            this.buttonCalculate.Size = new System.Drawing.Size(260, 30);
            this.buttonCalculate.TabIndex = 2;
            this.buttonCalculate.Text = "Tính tiền điện";
            this.buttonCalculate.Click += new System.EventHandler(this.buttonCalculate_Click);
            // 
            // Form1
            // 
            this.ClientSize = new System.Drawing.Size(300, 152);
            this.Controls.Add(this.textBoxKwh);
            this.Controls.Add(this.labelResult);
            this.Controls.Add(this.buttonCalculate);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "Tính Tiền Điện";
            this.ResumeLayout(false);
            this.PerformLayout();

        }
    }
}

