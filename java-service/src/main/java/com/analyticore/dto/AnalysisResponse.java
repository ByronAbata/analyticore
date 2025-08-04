package com.analyticore.dto;

public class AnalysisResponse {
  private String jobId;
  private double sentimentScore;
  private String[] keywords;

  public AnalysisResponse(String jobId, double sentimentScore, String[] keywords) {
    this.jobId = jobId;
    this.sentimentScore = sentimentScore;
    this.keywords = keywords;
  }

  public String getJobId() { return jobId; }
  public double getSentimentScore() { return sentimentScore; }
  public String[] getKeywords() { return keywords; }
}
