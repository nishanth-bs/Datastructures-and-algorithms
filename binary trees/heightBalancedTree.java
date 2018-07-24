private static class BalanceStatusWithHeight{
	boolean balanced;
	int height;
	public balancedStatusWithHeight(boolean balanced, int height){
		this.balanced = balanced;
		this.height = height;
	}
}

static boolean isBalanced( BinaryTreeNode<Integer> tree){
	return checkBalanced(tree).balanced;
}

static BalanceStatusWithHeight checkBalanced( BinaryTreeNode<Integer> tree){
	if(tree == null){ //base case
		return new BalanceStatusWithHeight(true, -1);
	}
	
	BalanceStatusWithHeight leftRes = checkBalanced(tree.left);
	if(!leftRes){
		return leftRes;		//left subtree is not balanced
	}

	BalanceStatusWithHeight rightRes = checkBalanced(tree.right);
	if(!rightRes){
		return rightRes;
	}

	boolean isBalanced = Math.abs(leftRes.height - rightRes.height) <= 1;
	int height = Math.max(leftRes.height, rightRes.height) + 1;
	return new BalanceStatusWithHeight( isBalanced, height);
}

class heightBalancedTree{
	public static void main(String[] args){
		BinaryTreeNode<Integer> a = new BinaryTreeNode

