using System;
using System.Linq;
using System.Collections.Generic;

using Xunit;
using FluentAssertions;

using Simpsons;
using Simpsons.Models;

namespace Simpsons.Test
{
    public class Tests
    {
        public Tests()
        {
            _result = _parser.Parse();
        }

        private ParseResult _result;
        private Parser _parser = new Parser();

        [Fact]
        public void Name()
        {
            _result.Name.Should().Be("Mr Homer J Simpson");
        }

        [Fact]
        public void Children()
        {
            _result.Children.Should().ContainEquivalentOf(new Child {
                Name="Bart Simpson",
                Age=9
            });
            _result.Children.Should().ContainEquivalentOf(new Child {
                Name="Lisa Simpson",
                Age=7
            });
        }

        [Fact]
        public void Address()
        {
            _result.Address.Postcode.Should().Be("SP14AS");
            _result.Address.PostalArea.Should().Be("SP");
            _result.Address.HouseNumber.Should().Be(742);
            _result.Address.Street.Should().Be("Evergreen Terrace");
            _result.Address.Town.Should().Be("Springfield");
        }

        [Fact]
        public void Dob()
        {
            _result.YearOfBirth.Should().Be(1960);
        }

        [Fact]
        public void Friends()
        {
            _result.Friends.Should().Contain("Moe");
            _result.Friends.Should().Contain("Barney");
            _result.Friends.Should().NotContain("Ned");
        }

        [Fact]
        public void BrandPreferences()
        {
            _result.BrandPreferences.Should().Contain(new KeyValuePair<string, string>("Duff", "Beer"));
            _result.BrandPreferences.Should().Contain(new KeyValuePair<string, string>("Moe's Tavern", "Bar"));
        }

        [Fact]
        public void Family()
        {
            _result.Family.Should().Contain(new KeyValuePair<string, string>("Marge Simpson", "Wife"));
            _result.Family.Should().Contain(new KeyValuePair<string, string>("Bart Simpson", "Child"));
            _result.Family.Should().Contain(new KeyValuePair<string, string>("Lisa Simpson", "Child"));
            _result.Family.Should().Contain(new KeyValuePair<string, string>("Abe Simpson", "Father"));
            _result.Family.Should().Contain(new KeyValuePair<string, string>("Selma Bouvier", "Sister-In-Law"));
            _result.Family.Should().Contain(new KeyValuePair<string, string>("Patty Bouvier", "Sister-In-Law"));
        }

        [Fact]
        public void PerformanceReview()
        {
            _result.PerformanceReviewAverageScore.Should().Be(1);
        }
    }
}
