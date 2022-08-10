#include <stdio.h>

char puzzle[9][9] = {
    {5,3,0,0,7,0,0,0,0},
    {6,0,0,1,9,5,0,0,0},
    {0,9,8,0,0,0,0,6,0},
    {8,0,0,0,6,0,0,0,3},
    {4,0,0,8,0,3,0,0,1},
    {7,0,0,0,2,0,0,0,6},
    {0,6,0,0,0,0,2,8,0},
    {0,0,0,4,1,9,0,0,5},
    {0,0,0,0,8,0,0,7,9}
};

char is_free(int *x , int *y){
    for(int i = 0; i<9;i++){
        for(int j =0 ; j<9;j++){
            if(puzzle[i][j]==0){
                *x = i;
                *y = j;
                return 1;
            }
        }
    }
    return 0;
    
}

char is_valid(int n , int x , int y){
    for(int i = 0; i<9;i++){
        if(puzzle[i][y] == n || puzzle[x][i] == n){
            return 0;
        }
    int square_x = (x/3)*3;
    int square_y = (y/3)*3;
    for(int i=square_x;i<square_x+3;i++){
        for(int j=square_y;j<square_y+3;j++){
            if(puzzle[i][j]==n){
                return 0;
            }
        }
    }
}
    return 1;

}

void draw(){
    for(int i = 0; i<9;i++){
        for(int j =0 ; j<9;j++){
            printf("%d ",puzzle[i][j]);
            }
        printf("\n");
        }
        
}

int solve(){
    int x,y;
    if(is_free(&x,&y)==0){
        return 1;
    }
    for(int n = 1;n<=9;n++){
        if(is_valid(n,x,y)==1){
            puzzle[x][y] = n;
            if(solve()==1){
                return 1;
            }
            puzzle[x][y] = 0;
        }
    }
    return 0;
}

int main(){
    if(solve()==0){
        printf("\nSorry that's unsolvable");
        return 0;
    };
    draw();

    return 0;
}