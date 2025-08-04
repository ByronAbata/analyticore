package com.analyticore.dto;

public class AnalysisRequest {
  private String jobId;
  private String text;

  public String getJobId() { return jobId; }
  public void setJobId(String jobId) { this.jobId = jobId; }

  public String getText() { return text; }
  public void setText(String text) { this.text = text; }
}
