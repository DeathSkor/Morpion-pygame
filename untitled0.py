import pygame
import time
surf= pygame.display.set_mode((300,300))
White=[255,255,255]
Black=[0,0,0]
Red=[255,0,0]
surf.fill(White)
pygame.display.update()
run=True
clock=pygame.time.Clock()
image1=pygame.image.load("./lib/cross_b.png")
image2=pygame.image.load("./lib/circle_b.png")
image3=pygame.image.load("./lib/cross_r.png")
image4=pygame.image.load("./lib/circle_r.png")
morp=[[0,0,0],
      [0,0,0],
      [0,0,0]]
pygame.draw.line(surf,Black,(100,0),(100,300),2)
pygame.draw.line(surf,Black,(200,0),(200,300),2)
pygame.draw.line(surf,Black,(0,100),(300,100),2)
pygame.draw.line(surf,Black,(0,200),(300,200),2)
pygame.display.flip()
clock.tick(60)
x=0
def test():
    s=0
    for a in range(3):
        s=0
        for b in range(3):
            s+=morp[a][b]
            if s==3:
                for z in range(3):
                    surf.blit(image3,(a*100,z*100))
                    pygame.display.flip()
                return 1
            elif s==-3:
                for z in range(3):
                    surf.blit(image4,(a*100,z*100))
                    pygame.display.flip()
                return -1
    for b in range(3):
        s=0
        for a in range(3):
            s+=morp[a][b]
            if s==3:
                for z in range(3):
                    surf.blit(image3,(z*100,b*100))
                    pygame.display.flip()
                return 1
            elif s==-3:
                for z in range(3):
                    surf.blit(image4,(z*100,b*100))
                    pygame.display.flip()
                return -1
    s= morp[0][0]+morp[1][1]+morp[2][2]

    if s==3:
        for z in range(3):
            surf.blit(image3,(z*100,z*100))
            pygame.display.flip()
        return 1
    elif s==-3:
        for z in range(3):
            surf.blit(image4,(z*100,z*100))
            pygame.display.flip()
        return -1
    s= morp[0][2]+morp[1][1]+morp[2][0]
    if s==3:
        surf.blit(image3,(0,200))
        surf.blit(image3,(100,100))
        surf.blit(image3,(200,0))
        pygame.display.flip()
        return 1
    elif s==-3:
        surf.blit(image4,(0,200))
        surf.blit(image4,(100,100))
        surf.blit(image4,(200,0))
        pygame.display.flip()
        return -1
    pygame.display.flip()
    return 0
            
        
                
while run:

    




    
    
    
    
    
    

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(3):
                if i*100<event.pos[0]<(i+1)*100:
                    for p in range(3):
                        if p*100<event.pos[1]<(p+1)*100:
                            if morp[i][p]==0:
                                if x%2==0:
                                    morp[i][p]=1
                                    surf.blit(image1,(i*100,p*100))
                                    pygame.display.flip()
                                    x+=1
                                else:
                                    morp[i][p]=-1
                                    surf.blit(image2,(i*100,p*100))
                                    pygame.display.flip()
                                    x+=1
                                
    if x==9 or test()!=0:
        time.sleep(10)
        run=False

    
                                    
                            
        

            

    
    
pygame.quit()        