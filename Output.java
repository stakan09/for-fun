class Kintore{

    String parts = "Chest";
    String type = "Normal";
    int weights = 80;
    int reps1 = 10;
    int reps2 = 3;

    public void printRecord() {

        String parts = "Arms";
        System.out.println("ローカル変数parts:" + parts);
        System.out.println("クラス変数parts:" + this.parts);
        System.out.println("ローカル変数type:" + type);
        System.out.println("クラス変数type:" + this.type);
    }
        
    public static void main(String[] args){
        Kintore day1 = new Kintore();
        day1.parts = "Legs";
        day1.weights = 110;
        System.out.println(day1.parts);
        System.out.println(day1.weights);
        day1.printRecord();
    }
}