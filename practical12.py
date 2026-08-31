    from pyspark.sql import SparkSession

    # 1. Initialize SparkSession
    spark = SparkSession.builder \
        .appName("JoinCSVAndWriteOutput") \
        .getOrCreate()

    # 2. Read the first CSV file (Employees)
    emp_df = spark.read.csv("employees.csv", header=True, inferSchema=True)

    # 3. Read the second CSV file (Departments)
    dept_df = spark.read.csv("departments.csv", header=True, inferSchema=True)

    # Display input DataFrames
    print("--- Employees DataFrame ---")
    emp_df.show()

    print("--- Departments DataFrame ---")
    dept_df.show()

    # 4. Join the two DataFrames on the common column 'dept_id'
    joined_df = emp_df.join(dept_df, on="dept_id", how="inner")

    print("--- Joined DataFrame ---")
    joined_df.show()

    # 5. Write the output DataFrame to a CSV file folder
    # 'coalesce(1)' saves the output as a single merged CSV file
    joined_df.coalesce(1).write \
        .option("header", "true") \
        .mode("overwrite") \
        .csv("output_joined_data")

    # 6. Stop the SparkSession
    spark.stop()