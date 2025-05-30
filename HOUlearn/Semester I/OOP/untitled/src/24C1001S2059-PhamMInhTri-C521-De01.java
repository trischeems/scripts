//// ## Ma sinh vien : 24C1001S2059
//// ## Ho ten : Pham Minh Tri
//// ## Lop : C521
//// ## ma de : de 01
//
//import java.io.*;
//import java.util.ArrayList;
//import java.util.Scanner;
//import java.text.NumberFormat;
//import java.util.Locale;
//
//class PHUKIEN {
//    protected String MaPK;
//    protected String TenPK;
//    protected String MauSac;
//
//    public PHUKIEN() {}
//
//    public PHUKIEN(String MaPK, String TenPK, String MauSac) {
//        this.MaPK = MaPK;
//        this.TenPK = TenPK;
//        this.MauSac = MauSac;
//    }
//
//    public void nhap() {
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap vao ma phu kien : ");
//        MaPK = sc.nextLine();
//        System.out.print("Nhap vao ten phu kien : ");
//        TenPK = sc.nextLine();
//        System.out.print("Nhap vao mau sac cua phu kien : ");
//        MauSac = sc.nextLine();
//    }
//
//    public void xuat(PrintWriter writer) {
//        writer.printf("Ma PK: %s\nTen PK: %s\nMau sac: %s\n", MaPK, TenPK, MauSac);
//    }
//}
//
//class TAINGHE extends PHUKIEN {
//    private String loai;
//    private int soLuongMua;
//    private double donGiaBan;
//
//    public TAINGHE() {}
//
//    public TAINGHE(String MaPK, String TenPK, String MauSac, String loai, int soLuongMua, double donGiaBan) {
//        super(MaPK, TenPK, MauSac);
//        this.loai = loai;
//        this.soLuongMua = soLuongMua;
//        this.donGiaBan = donGiaBan;
//    }
//
//    public void nhap() {
//        super.nhap();
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap loai tai nghe : ");
//        loai = sc.nextLine();
//        System.out.print("Nhap so luong mua : ");
//        soLuongMua = Integer.parseInt(sc.nextLine());
//        System.out.print("Nhap vao don gia : ");
//        donGiaBan = Double.parseDouble(sc.nextLine());
//    }
//
//    public double thanhTien() {
//        return soLuongMua * donGiaBan;
//    }
//
//    public void xuat(PrintWriter writer) {
//        super.xuat(writer);
//        NumberFormat currencyFormatter = NumberFormat.getCurrencyInstance(new Locale("vi", "VN"));
//        writer.printf("Loai : %s\nSo luong mua : %d\nDon gia ban : %s\nThanh tien : %s\n\n",
//                loai, soLuongMua, currencyFormatter.format(donGiaBan), currencyFormatter.format(thanhTien()));
//    }
//}
//
//class Main {
//    private ArrayList<TAINGHE> danhSachTaiNghe = new ArrayList<>();
//    public void nhapDanhSach() {
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Nhap so luong tai nghe : ");
//        int soluong = Integer.parseInt(sc.nextLine());
//
//        for (int i = 0; i < soluong; i++) {
//            System.out.println("Nhap thong tin tai nghe " + (i + 1));
//            TAINGHE tainghe = new TAINGHE();
//            tainghe.nhap();
//            danhSachTaiNghe.add(tainghe);
//        }
//    }
//
//    public void xuatDanhSach() {
//        System.out.println("\nDanh sach tai nghe : ");
//        for (TAINGHE tainghe : danhSachTaiNghe) {
//            tainghe.xuat(new PrintWriter(System.out, true));
//        }
//    }
//
//    public void luuDanhSachVaoFile(String tenFile) throws IOException {
//        try (PrintWriter writer = new PrintWriter(new BufferedWriter(new FileWriter(tenFile)))) {
//            for (TAINGHE tainghe : danhSachTaiNghe) {
//                tainghe.xuat(writer);
//            }
//        }
//    }
//
//    public double tinhTongTien() {
//        double tongTien = 0;
//        for (TAINGHE tainghe : danhSachTaiNghe) {
//            tongTien += tainghe.thanhTien();
//        }
//        return tongTien;
//    }
//
//    public static void main(String[] arg) {
//        Main tn = new Main();
//
//        tn.nhapDanhSach();
//        tn.xuatDanhSach();
//
//        NumberFormat currencyFormatter = NumberFormat.getCurrencyInstance(new Locale("vi", "VN"));
//        System.out.printf("\nTong tien hoa don tai nghe : %s\n", currencyFormatter.format(tn.tinhTongTien()));
//
//        try {
//            tn.luuDanhSachVaoFile("tainghe.dat");
//        } catch (IOException e) {
//            System.out.println("Loi khi luu file " + e.getMessage());
//        }
//    }
//}
