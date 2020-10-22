#include <vector>
#include <algorithm>
using namespace std;
vector<vector<int>> matrix;
vector<vector<int>> visited(102,vector<int>(102,0));
int dx[] = {-1,0,0,1};
int dy[] = {0,1,-1,0};
int maxrow;
int maxcol;
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int dfs(int row, int col){
    int res = 1;
    visited[row][col]=1;
    //printf("[%d][%d]\n",row,col);
    for(int i=0;i<4;i++){
        int drow = row+dx[i];
        int dcol = col+dy[i];
        if(drow>=maxrow || drow<0 || dcol>=maxcol || dcol<0) continue;
        if(visited[drow][dcol]) continue;
        if(matrix[row][col]==matrix[drow][dcol])
            res += dfs(drow,dcol);
    }
    return res;
}
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    int ret = 0;
    matrix = picture;
    maxrow = m;
    maxcol = n;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            visited[i][j]=0;
        }
    }
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(visited[i][j] == 0 && picture[i][j] != 0){
                number_of_area++;
                ret = dfs(i,j);
                max_size_of_one_area = max_size_of_one_area < ret ? ret : max_size_of_one_area;
            }
        }
    }
    //number_of_area = area.size();
    //max_size_of_one_area = *max_element(area.begin(), area.end());
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}