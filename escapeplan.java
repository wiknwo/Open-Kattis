// TODO: PRIMARY WORK! NOT FINISHED FOR ALL TEST CASES.

package com.company;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static final int SPEED = 10;

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        StringTokenizer st = new StringTokenizer(in.readLine());

        int scenario = 0;
        int numRobots = Integer.parseInt(st.nextToken());
        while (numRobots != 0) {
            System.out.println("Scenario " + ++scenario);
            
            double[][] robotCords = new double[numRobots][2];
            for (int i = 0; i < numRobots; i++) {
                st = new StringTokenizer(in.readLine());
                robotCords[i][0] = Double.parseDouble(st.nextToken());
                robotCords[i][1] = Double.parseDouble(st.nextToken());
            }

            st = new StringTokenizer(in.readLine());
            int numHoles = Integer.parseInt(st.nextToken());
            double[][] holeCords = new double[numHoles][2];
            for (int i = 0; i < numHoles; i++) {
                st = new StringTokenizer(in.readLine());
                holeCords[i][0] = Double.parseDouble(st.nextToken());
                holeCords[i][1] = Double.parseDouble(st.nextToken());
            }

            int[] underSpeeds = new int[3];

            for (int i = 0; i < numHoles; i++) {
                double minDistance = Integer.MAX_VALUE;
                int minRobot = -1;
                for (int j = 0; j < numRobots; j++) {
                    if (robotCords[j][0] == -1) continue;
                    double distance = Math.abs(holeCords[i][0] - robotCords[j][0]) + Math.abs(holeCords[i][1] - robotCords[j][1]);
                    if (distance < minDistance) {
                        minRobot = j;
                        minDistance = distance;
                    }
                }
                double minTime = minDistance / SPEED;
                if (minTime <= 5) underSpeeds[0]++;
                if (minTime <= 10) underSpeeds[1]++;
                if (minTime <= 20) underSpeeds[2]++;
                if(minRobot != -1) robotCords[minRobot][0] = -1;
            }

            System.out.println("In 5 seconds " + underSpeeds[0] + " robot(s) can escape");
            System.out.println("In 10 seconds " + underSpeeds[1] + " robot(s) can escape");
            System.out.println("In 20 seconds " + underSpeeds[2] + " robot(s) can escape");
            System.out.println("");
            st = new StringTokenizer(in.readLine());
            numRobots = Integer.parseInt(st.nextToken());
        }
    }
}
