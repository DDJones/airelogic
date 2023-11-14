using System.Collections.Generic;

namespace Simpsons.Models
{
    public class ParseResult
    {
        public string Name { get; set; }
        public Child[] Children { get; set; }
        public Address Address { get; set; }
        public int YearOfBirth { get; set; }
        public string[] Friends { get; set; }
        public Dictionary<string, string> BrandPreferences { get; set; }
        public Dictionary<string, string> Family { get; set; }
        public int PerformanceReviewAverageScore { get; set; }
    }
}