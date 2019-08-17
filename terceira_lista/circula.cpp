#include <stdio.h>
#include <math.h>

main(){
	int r = 5, p, x, y;
	
	printf("(0,%d)\n",r);
	
	p = 1-r;
	
	x = 0;
	y = r;
	while(x < y){
		if(p < 0){
			x++;
			p = p + 2*x + 1;
            printf("%d\n",p);
		}
		else if(p >=0){
			x++;
			y--;
			p = p + 2*x - 2*y + 1;
            
		}

		// printf("(%d,%d)\n",	x,y);
		// printf("(%d,%d)\n", y, x);
		// printf("(%d,%d)\n", y, -x);
		// printf("(%d,%d)\n", x, -y);
		// printf("(%d,%d)\n", -x, -y);
		// printf("(%d,%d)\n", -y, -x);
		// printf("(%d,%d)\n", -y, x);
		// printf("(%d,%d)\n", -x, y);
	}
}
