////
////
////class HangHoa{
////    private String tenHH;
////    private int soLuong ;
////    private float donGia;
////    public String getTenHH(){
////        return tenHH;
////    }
////
////    public void setTenHH(String name){
////        this.tenHH = name;
////    }
////
////    public int getSoLuong(){
////        return soLuong;
////    }
////
////    public void setSoLuong(int sl){
////        this.soLuong = sl;
////    }
////
////    public float getDonGia(){
////        return donGia;
////    }
////
////    public void setDonGia(float dg){
////        this.donGia = dg;
////    }
////
////    public float getTotalValue(){
////        return soLuong * donGia;
////    }
////
////    public void displayInfo(){
////        System.out.println("Ten hang hoa : " + tenHH);
////        System.out.println("So luong : " + soLuong);
////        System.out.println("Don gia : " + donGia);
////        System.out.println("Gia tri tong : " + getTotalValue());
////    }
////
////    public static HangHoa getHangHoa(String tenHH, int soLuong, float donGia){
////        HangHoa hh = new HangHoa();
////        hh.setTenHH(tenHH);
////        hh.setSoLuong(soLuong);
////        hh.setDonGia(donGia);
////        return hh;
////    }
////}
////
////class Main{
////    public static void main(String[] arg){
////        HangHoa hangHoa = HangHoa.getHangHoa("Banh mi",10,5.0f);
////        hangHoa.displayInfo();
////    }
////}
////
////
////
////
////
////
////import java.util.Scanner;
////class HocSinh{
////    float diemTB;
////    void nhapHS(){
////        Scanner sc = new Scanner(System.in);
////        System.out.print("Nhap DTB :");
////        diemTB = sc.nextFloat();
////    }
////    void xuatHS(){
////        System.out.printf("%7.1f", diemTB);
////    }
////}
//
//
////import javax.swing.*;
////import java.awt.*;
////
////class BarChart extends JPanel {
////
////    @Override
////    protected void paintComponent(Graphics g) {
////        super.paintComponent(g);
////
////        // Thiết lập chiều rộng và chiều cao cột
////        int barWidth = 50;
////        int baseLine = 200;
////
////        // Giá trị cột với các màu tương ứng
////        drawBar(g, Color.RED, 120, 50, baseLine, barWidth);
////        drawBar(g, Color.BLUE, 60, 150, baseLine, barWidth);
////        drawBar(g, Color.GRAY, 100, 250, baseLine, barWidth);
////        drawBar(g, Color.PINK, 80, 350, baseLine, barWidth);
////    }
////
////    private void drawBar(Graphics g, Color color, int height, int x, int baseLine, int width) {
////        g.setColor(color);
////        g.fillRect(x, baseLine - height, width, height);
////        g.setColor(Color.BLACK);
////        g.drawString(String.valueOf(height), x + 10, baseLine - height - 5);  // Hiển thị giá trị của mỗi cột
////    }
////
////    public static void main(String[] args) {
////        JFrame frame = new JFrame("Bar Chart");
////        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
////        frame.setSize(500, 300);
////        frame.add(new BarChart());
////        frame.setVisible(true);
////    }
////}
//
////import java.io.PrintStream;
////import java.util.Scanner;
////import java.io.FileOutputStream;
////class sinhvien{
////    private String hoTen;
////    private int maSV;
////    private int diemTB;
////
////    public sinhvien(){}
////    public sinhvien(String hoTen, int maSV, int diemTB){
////        this.hoTen = hoTen;
////        this.maSV = maSV;
////        this.diemTB = diemTB;
////    }
////
////    public void nhap(){
////        Scanner sc =new Scanner(System.in);
////
////        System.out.print("Nhap vao ho ten sv : ");
////            hoTen = sc.nextLine();
////        System.out.print("Nhap vao ma sinh vien : ");
////            maSV = Integer.parseInt(sc.nextLine());
////        System.out.print("Nhap vao diem trung binh : ");
////            diemTB = Integer.parseInt(sc.nextLine());
////    }
////
////    public void xuat(PrintStream p){
////        p.printf("Ten sv : %s\n", hoTen);
////        p.printf("Ma sv : %d\n", maSV);
////        p.printf("Diem tb : %d\n", diemTB);
////    }
////
////}
////
////class Main{
////    public static void main(String[] arg) throws Exception{
////        sinhvien sv = new sinhvien();
////
////        sv.nhap();
////        try(PrintStream p = new PrintStream(new FileOutputStream("filetext.dat"))){
////            sv.xuat(p);
////            System.out.println("Da luu");
////        }
////    }
////}
//
//
//// #### bai toan co ban
//
//import java.util.Scanner;
//
//class nhapLieu {
//    public int a;
//    public int b;
//
//    public nhapLieu() {}
//
//    public nhapLieu(int a, int b) {
//        this.a = a;
//        this.b = b;
//    }
//
//    public void nhap() {
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap vao a : ");
//        a = sc.nextInt();
//        System.out.print("Nhap vao b : ");
//        b = sc.nextInt();
//        // Để tránh lỗi trong các lần quét sau, không cần đóng Scanner ở đây
//    }
//
//    public static void main(String[] arg) {
//        nhapLieu nl = new nhapLieu();
//        nl.nhap();
//
//        System.out.println("Tong : " + (nl.a + nl.b));
//        System.out.println("Hieu : " + (nl.a - nl.b));
//        System.out.println("Tich : " + (nl.a * nl.b));
//        System.out.println("Thuong : " + ((double) nl.a / nl.b));
//    }
//}

// kiem tra xem so bat ki co phai so nguyen khong
//import java.util.Scanner;
//class Main{
//    public static void main(String[] arg){
//        Scanner sc = new Scanner(System.in);
//
//        System.out.print("Nhap vao :");
//
//        int num = sc.nextInt();
//
//        if(isPrime(num)){
//            System.out.println(num + " la so nguyen to.");
//        }
//        else{
//            System.out.println(num + " khong la so nguyen to.");
//        }
//
//        sc.close();
//    }
//    public static boolean isPrime(int n){
//        if(n<= 1) return false;
//        for(int i = 2 ; i <= Math.sqrt(n);i++){
//            if(n % i == 0) return false;
//        }
//        return true;
//    }
//}

// in bang cuu chuong
//import java.io.*;
//import java.util.Scanner;
//
//class tinhtoan {
//    protected int a;
//    public tinhtoan(){}
//    public tinhtoan(int a){
//        this.a = a;
//    }
//    public void nhap(){
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap vao a : ");
//            a = sc.nextInt();
//    }
//    public void xuat(PrintWriter wt){
//        for(int i = 1; i<= a;i++){
//            wt.println("Bang cuu chuong cua so : " + i + " la :");
//            for(int j = 1; j<=a;j++){
//                wt.println(i + " x " + j + " = " + (i*j));
//            }
//            wt.println();
//        }
//    }
//}
//
//class Main{
//    public void luuDanhSach(String tenFile, tinhtoan tt) throws IOException{
//        try(PrintWriter wt = new PrintWriter((new BufferedWriter((new FileWriter(tenFile)))))){
//            tt.xuat(wt);
//        }
//    }
//    public static void main(String[] arg){
//        tinhtoan tt = new tinhtoan();
//        tt.nhap();
//        Main cc = new Main();
//
//        try{
//            cc.luuDanhSach("bangCuuChuong.txt", tt);
//        }catch (IOException e ){
//            System.out.println("Loi" + e.getMessage());
//        }
//
//
//    }
//}

// tinh giai thua cua 1 so
//import java.util.Scanner;
//
//class Main{
//    public static void main(String[] arg){
//        int a = 1;
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap vao a : ");
//        int num = sc.nextInt();
//        for(int i = 1; i <= num; i++){
//            a *= i;
//        }
//        System.out.println("Giai thua cua a la :" + a);
//        sc.close();
//    }
//}

// dao nguoc gia tri cua chuoi
//import java.util.Scanner;
//
//class Main{
//    public static void main(String[] arg){
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap vao chuoi so : ");
//        String in = sc.nextLine();
//        String rev = new StringBuilder(in).reverse().toString();
//        System.out.println("Chuoi dao nguoc la : " + rev);
//    }
//}

// ##### mang
//import java.util.Scanner;
//
//class Main{
//    public static void main(String[] arg){
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap so phan tu : ");
//        int n = sc.nextInt();
//        int[] arr = new int[n];
//
//        System.out.println("Nhap cac phan tu cua mang : ");
//        for(int i = 0;i <n;i++){
//            System.out.println("Phan tu "+(i + 1) + ":");
//            arr[i] = sc.nextInt();
//        }
//        int sum = 0, max = arr[0], min = arr[0];
//        for(int num : arr){
//            sum += num;
//            if(num > max) max = num;
//            if(num < min) min = num;
//        }
//        double ave = (double)sum/n;
//
//        System.out.println("Tong gia tri cac phan tu : " + sum);
//        System.out.println("Gia tri lon nhat : " + max);
//        System.out.println("Gia tri nho nhat : " + min);
//        System.out.println("Trung binh cac phan tu : " + ave);
//    }
//}

//// kiem tra so armstrong

//import java.util.Scanner;
//
//class Main{
//    public static void main(String[] arg){
//        Scanner sc =new Scanner(System.in);
//
//        System.out.print("Nhap vao so : ");
//        int num = sc.nextInt();
//        int temp = num, sum = 0;
//
//        int digits = String.valueOf(num).length();
//
//        while(temp>0){
//            int digit = temp % 10;
//            sum += Math.pow(digit, digits);
//            temp /= 10;
//        }
//        if(sum == num){
//            System.out.println(num + " la so armStrong.");
//        }else{
//            System.out.println(num + " khong phai la so armstrong");
//        }
//        sc.close();
//    }
//}

// hien thi thong tin sinh vien
//import java.io.*;
//import java.util.Scanner;
//
//class thongtinsinhvien{
//    protected String hoten;
//    protected int maHS;
//    protected double diemTB;
//    public thongtinsinhvien(){}
//    public thongtinsinhvien(String hoten, int maHS,double diemTB){
//        this.hoten = hoten;
//        this.maHS = maHS;
//        this.diemTB = diemTB;
//    }
//    public void nhap(){
//        Scanner sc = new Scanner(System.in);
//        System.out.println("Nhap vao ten hoc sinh : ");
//        hoten = sc.nextLine();
//        System.out.println("Nhap vao ma hoc sinh : ");
//        maHS = sc.nextInt();
//        System.out.println("Nhap vao diem trung binh : ");
//        diemTB = sc.nextDouble();
//    }
//    public boolean hocBong(){
//        return diemTB >= 8;
//    }
//    public void xuat(PrintWriter wt){
//        wt.println("Ten hoc sinh : " + hoten);
//        wt.println("Ma hoc sinh : " + maHS);
//        wt.println("Diem trung binh : " + diemTB);
//        if(hocBong()){
//            wt.println("Hoc sinh duoc hoc bong.");
//        }else{
//            wt.println("Hoc sinh khong duoc hoc bong.");
//        }
//    }
//
//}
//class Main{
//    public void luuDanhSach(String tenFile, thongtinsinhvien ttsv) throws IOException{
//        try(PrintWriter wt = new PrintWriter((new BufferedWriter((new FileWriter(tenFile)))))){
//            ttsv.xuat(wt);
//        }
//    }
//    public static void main(String[] arg){
//        thongtinsinhvien ttsv = new thongtinsinhvien();
//        ttsv.nhap();
//        Main m = new Main();
//        try {
//            m.luuDanhSach("Thongtin.txt", ttsv);
//        }catch (IOException e){
//            System.out.println("Loi" + e.getMessage());
//        }
//    }
//}
//

// tim so hoan hao
//import java.util.Scanner;
//
//class Main{
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//
//        System.out.print("Nhập một số nguyên dương: ");
//        int num = sc.nextInt();
//
//        System.out.println("Các số hoàn hảo từ 1 đến " + num + " là:");
//
//        for (int n = 1; n <= num; n++) {
//            int sum = 0;
//            for (int i = 1; i <= n / 2; i++) {
//                if (n % i == 0) {
//                    sum += i;
//                }
//            }
//            if (sum == n) {
//                System.out.println(n);
//            }
//        }
//        sc.close();
//    }
//}

//
//import java.util.ArrayList;
//
//class sach{
//    private String tieuDe;
//    private String tacGia;
//    private int namXuatBan;
//
//    public sach(String tieuDe, String tacGia, int namXuatBan){
//        this.tieuDe = tieuDe;
//        this.tacGia = tacGia;
//        this.namXuatBan = namXuatBan;
//    }
//    public boolean isOldBook(){
//        return namXuatBan < 2000;
//    }
//    public void hienThiThongTin(){
//        System.out.println("Tieu de : " + tieuDe);
//        System.out.println("Tac gia : " + tacGia);
//        System.out.println("Nam xuat ban : " + namXuatBan);
//        System.out.println("Sach cu : " + (isOldBook()? "Co" : "Khong"));
//    }
//}
//class ThuVien{
//    private ArrayList<sach> danhSachSach;
//    public ThuVien(){
//        danhSachSach = new ArrayList<>();
//    }
//    public void themSach(sach sa){
//        danhSachSach.add(sa);
//    }
//    public boolean hasOldBooks(){
//        for(sach sa : danhSachSach){
//            if(sa.isOldBook()){
//                return true;
//            }
//        }
//        return false;
//    }
//    public void hienThiDanhSach(){
//        for(sach sa : danhSachSach){
//            sa.hienThiThongTin();
//            System.out.println();
//        }
//    }
//}

//class Main{
//    public static void main(String[] arg){
//        ThuVien tv = new ThuVien();
//
//        sach sa1 = new sach("Lap trinh java", " Nguyen Van A", 1998);
//        sach sa2 = new sach("Thiet ke OOP","Tran Thi B", 2005);
//
//        tv.themSach(sa1);
//        tv.themSach(sa2);
//        tv.hienThiDanhSach();
//        System.out.println("Thu vien co sach cu : " + (tv.hasOldBooks()? "Co" : "Khong"));
//    }
//}

//import java.util.ArrayList;
//
//class HocSinh{
//    private String hoTen;
//    private int tuoi;
//    private String maHS;
//    public HocSinh(String hoTen, int tuoi, String maHS){
//        this.hoTen = hoTen;
//        this.maHS = maHS;
//        this.tuoi = tuoi;
//    }
//    public void hienThiThongTin(){
//        System.out.println("Hoc sinh : " + hoTen + ", Tuoi : " + tuoi + ", Ma HS : "+ maHS);
//    }
//}
//class GiaoVien{
//    private String hoTen;
//    private int tuoi;
//    private String maGV;
//    public GiaoVien(String hoTen, int tuoi, String maGV){
//        this.hoTen = hoTen;
//        this.tuoi = tuoi;
//        this.maGV = maGV;
//    }
//    public void hienThiThongTin(){
//        System.out.println("Hoc sinh : " + hoTen + ", Tuoi : " + tuoi + ", Ma GV : "+ maGV);
//    }
//}
//
//class MonHoc{
//    private String tenMH;
//    private GiaoVien GV;
//    public MonHoc(String tenMH, GiaoVien GV){
//        this.tenMH = tenMH;
//        this.GV = GV;
//    }
//    public void hienThiThongTin(){
//        System.out.println("Mon Hoc : " + tenMH);
//        GV.hienThiThongTin();
//    }
//}
//
//class LopHoc{
//    private ArrayList<HocSinh> danhSachHocSinh;
//    private ArrayList<MonHoc> danhSachMonHoc;
//    public LopHoc(){
//        danhSachHocSinh = new ArrayList<>();
//        danhSachMonHoc = new ArrayList<>();
//    }
//    public void themHocSinh(HocSinh hocSinh){
//        danhSachHocSinh.add(hocSinh);
//    }
//    public void themMonHoc(MonHoc monHoc){
//        danhSachMonHoc.add(monHoc);
//    }
//    public void hienThiDanhSachHocSinh(){
//        System.out.println("Danh sach hoc sinh : ");
//        for(HocSinh hs : danhSachHocSinh){
//            hs.hienThiThongTin();
//        }
//    }
//    public void hienThiDanhSachMonHoc(){
//        System.out.println("Danh sach mon hoc : ");
//        for(MonHoc mh : danhSachMonHoc){
//            mh.hienThiThongTin();
//        }
//    }
//}
//class Main{
//    public static void main(String[] arg){
//        LopHoc lh = new LopHoc();
//        HocSinh hs1 = new HocSinh("N V A", 15, "HS001");
//        HocSinh hs2 = new HocSinh("N V B", 16, "HS002");
//
//        GiaoVien gv = new GiaoVien("P V C", 40,"GV0001");
//        MonHoc mh1 = new MonHoc("Van", gv);
//
//        lh.themHocSinh(hs1);
//        lh.themHocSinh(hs2);
//        lh.themMonHoc(mh1);
//
//        lh.hienThiDanhSachHocSinh();
//        lh.hienThiDanhSachMonHoc();
//    }
//}
//
//
//import java.util.ArrayList;
//
//abstract class TaiKhoan{
//    protected  String soTaiKhoan;
//    protected double soDu;
//
//    public TaiKhoan(String soTaiKhoan, double soDu){
//        this.soDu = soDu;
//        this.soTaiKhoan = soTaiKhoan;
//    }
//
//    public void guiTien(double soTien){
//        soDu += soTien;
//        System.out.println(" Gui thanh cong : " + soTien);
//    }
//
//    public void rutTien(double soTien){
//        if(soDu >= soTien){
//            soDu -= soTien;
//            System.out.println("Rut tien thanh cong : " + soTien);
//        }else{
//            System.out.println("Khong du so du.");
//        }
//    }
//
//    public void hienThiSoDu(){
//        System.out.println("So du tai khoan " + soTaiKhoan + " : "+soDu);
//    }
//}
//
//class TaiKhoanTietKiem extends TaiKhoan{
//    private double laiSuat;
//
//    public TaiKhoanTietKiem(String soTaiKhoan, double soDu, double laiSuat){
//        super(soTaiKhoan, soDu);
//        this.laiSuat = laiSuat;
//    }
//
//    public void tinhLai(){
//        soDu += soDu * laiSuat;
//        System.out.println("Da cong lai xuat. SO du moi: " + soDu);
//    }
//}
//
//class TaiKhoanVangLai extends TaiKhoan{
//    public TaiKhoanVangLai(String soTaiKhoan, double soDu){
//        super(soTaiKhoan, soDu);
//    }
//}
//
//class Main{
//    public static void main(String[] arg){
//        TaiKhoanTietKiem tk1 = new TaiKhoanTietKiem("TK001", 5000,0.05);
//        TaiKhoanVangLai tk2 = new TaiKhoanVangLai("TK002", 5000);
//
//        tk1.guiTien(2000);
//        tk1.hienThiSoDu();
//        tk1.tinhLai();
//
//        tk2.rutTien(1000);
//        tk2.hienThiSoDu();
//    }
//}
















