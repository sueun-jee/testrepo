# Databricks notebook source
#Reposのテスト

# COMMAND ----------

# MAGIC %run ./libs/utilities

# COMMAND ----------

# MAGIC %run ./libs/api_caller

# COMMAND ----------

# MAGIC %run ./libs/operations

# COMMAND ----------

# MAGIC %md
# MAGIC API Caller呼び出し

# COMMAND ----------

# テスト用
test_api_caller = ApiCaller(base_url, API_HOST, API_KEY)
