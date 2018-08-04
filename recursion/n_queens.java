import java.util.*;

class n_queens{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("n*n?");
		int n = sc.nextInt();
		List<List<Integer>> res = nQueens(n);
		//System.out.println(solveNQueens(n));
		for(List<Integer> i : res){
			for(int j : i){
				System.out.print(i);
			}
			System.out.println();
		}
	}	
	public static List<List<Integer>> nQueens(int n){
		List<List<Integer>> res = new ArrayList<>();
		solveNQueens(n, 0, new ArrayList<Integer>(), res);
		return res;
	}
	static void solveNQueens(int n, int row, List<Integer> colPlacement, List<List<Integer>> res){
		if(row == n){
			res.add(new ArrayList<>(colPlacement)); //all the queens are legally placed
		}
		else{
			for(int col = 0; col < n; col++){
				colPlacement.add(col);
				if(isValid(colPlacement)){
					solveNQueens(n, row+1, colPlacement, res);
				}else{
					colPlacement.remove(colPlacement.size()-1);
				}
			}
		}
	}

	static boolean isValid(List<Integer> colPlacement){
		int rowId = colPlacement.size() -1;
		for(int i = 0; i< rowId; i++){
			int diff = Math.abs(colPlacement.get(i) - colPlacement.get(rowId));
			if(diff == 0 || diff == rowId - i){
				return false;
			}
		}
		return true;
	}
}
