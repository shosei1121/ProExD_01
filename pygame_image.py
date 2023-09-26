import sys
import pygame as pg

def main():
    # ゲームウィンドウのキャプションを設定する
    pg.display.set_caption("はばたけ！こうかとん")
    
    # ウィンドウサイズが800x600ピクセルのスクリーンオブジェクトを作成する
    screen = pg.display.set_mode((800, 600))
    
    # フレームレートを制御するためのクロックオブジェクトを作成する
    clock  = pg.time.Clock()
    
    # 背景画像をファイルから読み込む
    bg_img = pg.image.load("ProjExD2023/ex01/fig/pg_bg.jpg")
    bg_imge2= pg.transform.flip(bg_img, True, False)
    
    # キャラクター画像をファイルから読み込み、水平方向に反転させる
    kk_img = pg.image.load("ProjExD2023/ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    
    # キャラクター画像を回転し、拡大縮小する
    kk_img2= pg.transform.rotozoom(kk_img, 10, 1.0)
    
    # アニメーション用のキャラクター画像のリストを作成する
    kk_imgs = [kk_img, kk_img2]
    tmr=0
    count = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        x = tmr % 3200

        if 0 <= tmr % 500 < 250:
            i = 0
        else:
            i = 1
            
        screen.blit(bg_img, (-x, 0))
        screen.blit(bg_img, (-x+3200, 0))
        screen.blit(bg_imge2, (-x+1600, 0))
        screen.blit(kk_imgs[i],[300, 200])
        
        pg.display.update()
        tmr += 1.5
        count += 1
        
        if count == len(kk_imgs):
            count = 0
            
        clock.tick(200)  # フレームレートを60に設定する

if __name__ == "__main__":
    # pygameを初期化する
    pg.init()
    
    # main関数を呼び出す
    main()
    
    # pygameを終了し、プログラムを終了する
    pg.quit()
    sys.exit()
