package com.analyticore.service;

public class SentimentAnalysisService {
  public double analyzeSentiment(String text) {
    if (text.toLowerCase().contains("feliz") || text.contains("bien")) return 0.9;
    if (text.contains("mal") || text.contains("triste")) return 0.2;
    return 0.5;
  }
}
