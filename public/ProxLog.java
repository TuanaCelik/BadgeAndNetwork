import java.io.*;
import java.util.*;
import java.io.File;
import java.util.Scanner;
import java.util.Arrays;
import java.lang.*;
import java.io.PrintWriter;

public class ProxLog{
	
	static List<Integer> piggyBacks = new ArrayList<Integer>();
	static List<Integer> classified = new ArrayList<Integer>();
	static List<Integer> employees = new ArrayList<Integer>();
	static List<String> prox = new ArrayList<String>();

	public ProxLog() throws IOException{

		try{
			File in = new File("proxLog.csv");
			Scanner log = new Scanner(in);

			int flag = 0;
			while(log.hasNext()){
				String string = log.next();
				if(flag > 0){
					employees.add(Integer.parseInt(string.split(",")[0]));
					prox.add(string.split(",")[1]);
				}
				flag++;
			}
			log.close();
		}
		catch (FileNotFoundException e){
			System.out.println("Something went wrong!");
		}
	}

	public static void main(String args[]){
		try{
			ProxLog proxLog = new ProxLog();
			proxLog.findPiggies(employees,prox);
			PrintWriter pw = new PrintWriter(new File("piggy.csv"));
	        StringBuilder sb = new StringBuilder();
	        sb.append("id");
	        sb.append(',');
	        sb.append("piggyNum");
	        sb.append('\n');
	        for(int i = 0; i < piggyBacks.size(); i++){
	        	sb.append(i);
	        	sb.append(',');
	        	sb.append(piggyBacks.get(i));
	        	sb.append('\n');
	        }
	        pw.write(sb.toString());
        	pw.close();

		}
		catch (IOException e){
			System.out.println("Problem with file input.");
		}
	}

	public void findPiggies(List<Integer> employees, List<String> prox){
		for(int i = 0; i < 60; i++){
			Integer proxNum = findNum(i);
			piggyNum(i, proxNum, prox);			
		}
		//System.out.println(piggyBacks.size());
	}

	public Integer findNum(Integer id){
		Boolean flag = true;
		int index = 0;
		Integer proxNum = 0;

		while(flag){
			if(employees.size() > 0 && employees.get(0) == id){ 
				proxNum++;
				employees.remove(0); 
			}else flag = false;
		}
		return proxNum;
	}

	public void piggyNum(Integer id, Integer num, List<String> prox){
		int ind = 0;
		int build = 0;
		for(int i = 0; i < num; i++){
			if(prox.get(i).equals("prox-in-classified")){
				classified.add(ind, 1);
				build = 1;
				ind++;
			}
			else if(prox.get(i).equals("prox-out-classified") && build == 1){
				classified.remove(ind-1);
				ind--;
				build = 0;
			}
			else if(prox.get(i).equals("prox-out-classified") && build == 0){
				classified.add(ind,1);
				build = 0;
				ind++;
			}
		}
		for(int i = 0; i < num; i++) prox.remove(0);
		piggyBacks.add(id, classified.size());
		classified = new ArrayList<Integer>();
	}
}