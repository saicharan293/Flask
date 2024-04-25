using System;
using IronPython.Compiler.Ast;
using Python.Runtime;

namespace PythonIntegration
{
    class Program
    {
        static void Main(string[] args)
        {
            Environment.SetEnvironmentVariable("PYTHONNET_PYDLL", @"D:\1Python\python312.dll");
            PythonEngine.Initialize();

            dynamic sys = Py.Import("sys");
            string path =sys.path.append(@"D:\Downloads\dotnet\pdfReader");
            dynamic pdf = Py.Import("task");
            using (Py.GIL())
            {
                bool flag = true;
                while(flag)
                {

                    string pdfFilePath = @"D:\Downloads\dotnet\pdfReader\sample.pdf";

                    Console.Write("Hello user, choose your favorite page ");
                    int choice = int.Parse(Console.ReadLine());

                    dynamic pdf_encode = pdf.pdf_encode(pdfFilePath);

                    dynamic page_data_tuple = pdf.get_required_Data(pdf_encode, choice - 1);
                    dynamic page_data = page_data_tuple[0];
                    string error_message = page_data_tuple[1];
                    if (page_data != null)
                    {
                        string outputDir = @"D:\Downloads\dotnet\pdfReader";
                        pdf.required_page(page_data, outputDir + @"\decoded.pdf");
                        Console.WriteLine("Page has been saved as 'decoded.pdf' " + outputDir);
                    

                    }
                    else
                    {
                        Console.WriteLine(error_message);
                        Console.WriteLine("Invalid page number, please choose a valid page number");
                    }
                    Console.Write("Do you want to continue (y/n)? ");
                    string continueChoice = Console.ReadLine().ToLower();
                    flag = continueChoice == "y";

                }
            }
        }
    }
}



//byte[] pdfBin = System.IO.File.ReadAllBytes(@"D:\Downloads\dotnet\pdfReader\sample.pdf");
// string pdfEncode = Convert.ToBase64String(pdfBin);