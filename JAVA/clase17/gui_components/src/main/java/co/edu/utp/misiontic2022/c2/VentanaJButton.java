package co.edu.utp.misiontic2022.c2;
import java.awt.Container;
import java.awt.*;

import javax.swing.JButton;
import javax.swing.JFrame;

public class VentanaJButton  extends JFrame{
    
    public VentanaJButton(){
        Container c = getContentPane();
        c.setLayout(new FlowLayout());
        //
        JButton b1 = new JButton("Aceptar!");
        JButton b2 = new JButton("Aceptar!");
        c.add(b1);
        c.add(b2);
        
        this.setLocationRelativeTo(null);
        setSize(300, 300);
        setVisible(true);
    }

    public static void main(String[] args) {
        new VentanaJButton();
    }
    
}
